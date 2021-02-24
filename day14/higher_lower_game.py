import higher_lower_art
import higher_lower_data
import random


# functions

def random_num():
    n1 = random.randint(0, len(data))
    return n1


def play(score):
    global b_participant
    score += 1
    a_participant = random_num()
    if score > 0:
        a_participant = b_participant
        print(f"You're right! Current score: {score}")
    b_participant = random_num()
    print(f"Compare A: {data[a_participant]['name']}, "
          f"a {data[a_participant]['description']}, "
          f"from {data[a_participant]['country']}")
    print(higher_lower_art.vs)
    print(f"Compare B: {data[b_participant]['name']}, "
          f"a {data[b_participant]['description']}, "
          f"from {data[b_participant]['country']}")
    compare(a_participant, b_participant, score)


def compare(a_participant, b_participant, score):
    a_participant_followers = data[a_participant]['follower_count']
    b_participant_followers = data[b_participant]['follower_count']
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if (guess == 'A' and a_participant_followers > b_participant_followers) or (
            guess == 'B' and b_participant_followers > a_participant_followers):
        play(score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


# actual game

data = higher_lower_data.data
b_participant = random_num()

print(higher_lower_art.logo)
still_playing = True
starting_score = -1

while still_playing:
    play(starting_score)
    still_playing = False
