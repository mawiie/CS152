:- dynamic known/2, known/3.

% Restaurant recommendation criteria
within_budget(AvgMealPrice) :-
    user_budget(MaxBudget),
    AvgMealPrice =< MaxBudget.
user_budget(Value) :- get_single(user_budget, Value).

acceptable_wait_time(WaitTime) :-
    user_max_wait_time(MaxWait),
    WaitTime =< MaxWait.
user_max_wait_time(Value) :- get_single(user_max_wait_time, Value).

acceptable_distance(DistanceKm) :-
    user_max_distance(MaxDistance),
    DistanceKm =< MaxDistance.
user_max_distance(Value) :- get_single(user_max_distance, Value).

acceptable_rating(Rating) :-
    user_min_rating(MinRating),
    Rating >= MinRating.
user_min_rating(Value) :- get_single(user_min_rating, Value).

sufficient_ratings(NumRatings) :-
    user_min_num_ratings(MinNum),
    NumRatings >= MinNum.
user_min_num_ratings(Value) :- get_single(user_min_num_ratings, Value).

% A restaurant satisfies payment condition if one of its payment methods is the same as users preferred payment method
acceptable_payment(PaymentOptions) :-
    user_payment_preference(PaymentMethod),
    member(PaymentMethod, PaymentOptions),
    !.
payment_option(card).
payment_option(cash).
payment_option(mobile).
user_payment_preference(Value) :- payment_option(Value), get_yesno(user_payment_preference, Value).

% If user has no dietary restriction, all restaurants meets the need
meets_dietary_needs(_) :-
    get_yesno(user_dietary_restriction, none),
    !.
% Else if user has dietary restriction, check if that diet is supported by this restaurant
meets_dietary_needs(DietaryOptions) :-
    \+ (DietaryOptions = []),    % If user has dietary restriction but this restaurant offers no other dietary options (e.g. vegetarian), it fails.
    user_dietary_restriction(Restriction),
    member(Restriction, DietaryOptions),
    !.
dietrary_option(none).
dietrary_option(vegan).
dietrary_option(vegetarian).
dietrary_option(halal).
user_dietary_restriction(vegetarian) :- user_dietary_restriction(vegan).    % Vegans are vegetarians
user_dietary_restriction(Value) :- dietrary_option(Value), get_yesno(user_dietary_restriction, Value).

matches_cuisine(Cuisine) :-
    user_cuisine_preference(Cuisine).
user_cuisine_preference(Value) :- get_yesno(user_cuisine_preference, Value).

recommend(Restaurant) :-
    restaurant(Restaurant, AvgMealPrice, Cuisine, WaitTime, DietaryOptions, DistanceKm, Rating, NumRatings, PaymentOptions),
    within_budget(AvgMealPrice),
    acceptable_wait_time(WaitTime),
    acceptable_distance(DistanceKm),
    acceptable_rating(Rating),
    sufficient_ratings(NumRatings),
    acceptable_payment(PaymentOptions),
    meets_dietary_needs(DietaryOptions),
    matches_cuisine(Cuisine).
    
get_single(Attribute, Value) :- known(Attribute, Value), !.
get_single(Attribute, Value) :- known(Attribute, Value2), Value \== Value2, !, fail.
get_single(Attribute, Value) :- ask_single(Attribute, Response), assertz(known(Attribute, Response)), get_single(Attribute, Value).

get_yesno(Attribute, Value) :- known(yes, Attribute, Value), !.
get_yesno(Attribute, Value) :- known(_, Attribute, Value), !, fail.
get_yesno(Attribute, Value) :- ask_yesno(Attribute, Value, Response), assertz(known(Response, Attribute, Value)), Response == yes.