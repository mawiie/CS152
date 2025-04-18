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
    
    # Special handling for cuisine preference
    if attr == 'user_cuisine_preference':
        if hasattr(ask_yesno, 'collection_mode') and ask_yesno.collection_mode:
            # Collection mode: collect cuisine and always say "yes" temporarily
            if not hasattr(ask_yesno, 'collected_cuisines'):
                ask_yesno.collected_cuisines = set()
            
            ask_yesno.collected_cuisines.add(val)
            
            # Always respond "yes" during collection to explore all paths
            Response.unify(Atom('yes'))
            return True
        
        # Recommendation mode: use the real preferences
        elif hasattr(ask_yesno, 'selected_cuisines'):
            # Check if this cuisine was selected by the user
            if val in ask_yesno.selected_cuisines:
                Response.unify(Atom('yes'))
            else:
                Response.unify(Atom('no'))
            return True
    
    # Check if we've already asked this exact question
    question_key = (attr, val)
    if hasattr(ask_yesno, 'answered_questions') and question_key in ask_yesno.answered_questions:
        Response.unify(Atom(ask_yesno.answered_questions[question_key]))
        return True
    
    # Format question properly
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
            
            # Store the answer for future use
            if not hasattr(ask_yesno, 'answered_questions'):
                ask_yesno.answered_questions = {}
            ask_yesno.answered_questions[question_key] = reply
            
            Response.unify(Atom(reply))
            return True
        else:
            print("Please answer 'yes' or 'no'.")

ask_yesno.arity = 3
registerForeign(ask_yesno)

def run_restaurant_recommendations():
    # Initialize the Prolog KB and restaurant facts
    def list_to_prolog(lst):
        return "[" + ", ".join(lst) + "]"

    call(retractall(restaurant))
    for _, row in restaurant_df.iterrows():
        fact = f'restaurant("{row["name"]}", {row["price"]}, "{(row["cuisine"])}", {row["wait"]}, {list_to_prolog(row["diet"])}, {row["distance"]}, {row["rating"]}, {row["num_ratings"]}, {list_to_prolog(row["payment"])})'
        prolog.assertz(fact)

    call(retractall(known2))
    call(retractall(known3))
    
    # Initialize the question tracking
    if hasattr(ask_yesno, 'answered_questions'):
        delattr(ask_yesno, 'answered_questions')
    ask_yesno.answered_questions = {}

    print('Please enter your preferences and we will recommend you some restaurants!')

    # Collect all the cuisines based on partial query
    ask_yesno.collection_mode = True
    ask_yesno.collected_cuisines = set()
    
    collection_results = list(prolog.query("recommend(X)."))
    
    # Ready to recommend
    ask_yesno.collection_mode = False
    
    # Check if we have any cuisines collected
    if not ask_yesno.collected_cuisines:
        print("No cuisines matched your other preferences. Try adjusting your criteria.")
        return
    
    # Multi-choice menu
    cuisine_list = sorted(list(ask_yesno.collected_cuisines))
    print("\nBased on your preferences, we found these cuisine options:")
    for idx, cuisine in enumerate(cuisine_list, 1):
        print(f"{idx}. {cuisine}")
    
    print("\nEnter the numbers of cuisines you like (comma-separated, e.g., 1,3,5)")
    print("Or type 'all' to select all cuisines")
    
    # Get user selection
    while True:
        try:
            user_input = input("> ").strip().lower()
            
            # Handle 'all' selection
            if user_input == 'all':
                selected_cuisines = cuisine_list
                break
            
            # Process numeric selections
            selected_indices = [int(idx.strip()) for idx in user_input.split(',')]
            selected_cuisines = [cuisine_list[idx-1] for idx in selected_indices if 1 <= idx <= len(cuisine_list)]
            
            if not selected_cuisines:
                print("No valid cuisines selected. Please try again.")
                continue
            
            break
                
        except (ValueError, IndexError):
            print("Invalid input. Please enter comma-separated numbers or 'all'.")
    
    # Store the user's selections for ask_yesno to use
    ask_yesno.selected_cuisines = set(selected_cuisines)
    
    # Now complete the recommendation
    call(retractall(known3))  # Clear all known/3 facts
    
    for question_key, answer in ask_yesno.answered_questions.items():
        attr, val = question_key
        if attr != 'user_cuisine_preference':
            prolog.assertz(f"known({answer}, {attr}, '{val}')")
    
    # Run the recommendation query with the real preferences
    print("Finding restaurants that match your preferences...")
    results = list(prolog.query("recommend(X)."))
    
    # Process results
    names = [r["X"].decode() if isinstance(r["X"], bytes) else r["X"] for r in results]
    if len(names) > 0:
        filtered_df = restaurant_df[restaurant_df["name"].isin(names)].copy()
        sorted_df = filtered_df.sort_values(by="rating", ascending=False)
        print('We recommend:')
        for _, row in sorted_df.iterrows():
            print(f"- {row['name']} (Rating: {row['rating']}, Price: ${row['price']})")
    else:
        print("No restaurants matched all your preferences. Try adjusting your criteria and search again.")

# Call the recommendation function
run_restaurant_recommendations()
