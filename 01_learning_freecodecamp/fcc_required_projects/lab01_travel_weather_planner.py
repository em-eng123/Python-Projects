# -------------------------------------------------------------
# EVALUATION: Lab 01 - Build a Travel Weather Planner
# NOTES: Independent logic build implementing complex conditional branching and boolean operator chains.
# -------------------------------------------------------------

# USER STORIES TO FULFILL:
# 1. Create variables: distance_mi, is_raining, has_bike, has_car, has_ride_share_app
# 2. Use conditionals to determine if commuting is possible.
# 3. Evaluate distance categories in ascending order (if / elif / else).
# 4. Use at least one boolean operator (and, or, not).
# 5. If distance_mi is falsy -> print False.
# 6. If distance <= 1 mile -> print True only if not raining. Otherwise False.
# 7. If distance > 1 and <= 6 miles -> print True only if has bike and not raining. Otherwise False.
# 8. If distance > 6 miles -> print True if has car or ride-share app. Otherwise False.

# -------------------------------------------------------------

distance_mi = 2
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True
if not distance_mi:
    print("False")
elif distance_mi<=1:
    if not is_raining:
        print("True")
    else:    
        print("False")
elif distance_mi>1 and distance_mi<=6:
    if has_bike and not is_raining:
        print("True")
    else:
        print("False")
else:
    if has_car or has_ride_share_app:
        print("True")
    else:
        print("False")