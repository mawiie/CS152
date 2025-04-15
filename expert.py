from restaurants import restaurant_df

# The code here will ask the user for input based on the askables. It will only ask the user where necessary.

# Import necessary packages
import tempfile
from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog() # Global handle to interpreter

# Create a temporary file with the KB in it
name = 'kb.pl'
prolog.consult(name) # open the KB for consulting

retractall = Functor("retractall")
known2 = Functor("known", 2)
known3 = Functor("known", 3)
restaurant = Functor('restaurant', 9)

ask_single_value = {
    'user_budget': {
        'question': "What's the maximum you're willing to spend per meal? (in pesos)",
        'min': 1,
        'type': 'float'
    },
    'user_max_wait_time': {
        'question': "How long are you willing to wait for your food? (in minutes)",
        'min': 1,
        'type': 'float'
    },
    'user_max_distance': {
        'question': "How far are you willing to travel to eat out? (in kilometers)",
        'min': 0.1,
        'type': 'float'
    },
    'user_min_rating': {
        'question': "What's the minimum restaurant rating (1–5) you're comfortable with?",
        'min': 1.0,
        'max': 5.0,
        'type': 'float'
    },
    'user_min_num_ratings': {
        'question': "What's the minimum number of reviews a restaurant should have?",
        'min': 1,
        'type': 'int'
    }
}


ask_multivalued = {
    'user_payment_preference': {
        'question': "Do you accept paying with {value}?",
    },
    'user_dietary_restriction': {
        'question': "Do you follow a {value} diet?",
    },
    'user_cuisine_preference': {
        'question': "Are you interested in {value} cuisine?",
    }
}

def ask_single(Attribute, Value):
    attr = Attribute.value if isinstance(Attribute, Atom) else str(Attribute)
    config = ask_single_value.get(attr)

    question = config["question"]
    min_val = config.get("min", float('-inf'))
    max_val = config.get("max", float('inf'))
    expected_type = config.get("type", "float")

    while True:
        response = input(f"{question}\n> ").strip()
        try:
            if expected_type == "int":
                val = int(response)
            else:
                val = float(response)

            if val < min_val:
                print(f"Please enter a value ≥ {min_val}.")
            elif val > max_val:
                print(f"Please enter a value ≤ {max_val}.")
            else:
                Value.unify(val)
                return True

        except ValueError:
            print(f"Please enter a valid {'integer' if expected_type == 'int' else 'number'}.")

ask_single.arity = 2
registerForeign(ask_single)

def ask_yesno(Attribute, Value, Response):
    attr = Attribute.value if hasattr(Attribute, 'value') else str(Attribute)
    
    # Convert Value to string if it's an Atom or list of Atoms
    if isinstance(Value, list):
        val = [item.value if hasattr(item, 'value') else str(item) for item in Value]
    else:
        val = Value.value if hasattr(Value, 'value') else str(Value)
    
    config = ask_multivalued.get(attr)
    
    # Format question properly
    if attr == 'user_cuisine_preference':
        cuisine_name = val  # This should be a string now
        question = f"Are you interested in {cuisine_name} cuisine?"
    else:
        question = config["question"].format(value=val)
    
    # Handle special phrasing for 'none' dietary option
    flip_answer = False
    if attr == 'user_dietary_restriction' and val == 'none':
        question = "Do you have any dietary restrictions?"
        # When this question is asked, the answer "no" actually means "yes" to a "dietary restriction = none", and vice versa.
        flip_answer = True   
        
    while True:
        reply = input(f"{question} (yes/no):\n> ").strip().lower()
        if reply in {"yes", "no"}:
            if flip_answer:
                reply = 'yes' if reply == 'no' else 'no'
            Response.unify(Atom(reply))
            return True
        else:
            print("Please answer 'yes' or 'no'.")

ask_yesno.arity = 3
registerForeign(ask_yesno)

# Create a temporary file with the KB in it
name = 'kb.pl'
prolog.consult(name) # open the KB for consulting

def list_to_prolog(lst):
    return "[" + ", ".join(lst) + "]"

call(retractall(restaurant))
for _, row in restaurant_df.iterrows():
    fact = f'restaurant("{row["name"]}", {row["price"]}, {row["cuisine"]}, {row["wait"]}, {list_to_prolog(row["diet"])}, {row["distance"]}, {row["rating"]}, {row["num_ratings"]}, {list_to_prolog(row["payment"])})'
    prolog.assertz(fact)

call(retractall(known2))
call(retractall(known3))

print('Please enter your preferences and we will recommend you some restaurants!')
results = [s for s in prolog.query("recommend(X).")]

names = [r["X"].decode() if isinstance(r["X"], bytes) else r["X"] for r in results]
if len(names) > 0:
    filtered_df = restaurant_df[restaurant_df["name"].isin(names)].copy()
    sorted_df = filtered_df.sort_values(by="rating", ascending=False)
    print('We recommend:')
    for _, row in sorted_df.iterrows():
        print(f"- {row['name']} (Rating: {row['rating']}, Price: ${row['price']})")
else:
    print("No restaurants matched your preferences. Try adjusting your criteria and search again.")
