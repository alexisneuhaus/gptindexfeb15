import random
import openai
import os

os.environ["OPENAI_API_KEY"] = "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"
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

know_type = input("Do you know your Enneagram type? (yes/no)")
if know_type == "yes":
    type = input("What is your Enneagram type? (please type it in as a number, eg. 5)")
else:
    print("No worries, enjoy the Subtypes test!")
    type = "undetermined"

print('\n\nWelcome to the Instinctual Subtypes test!')
print('\nPlease answer each question with:')
print('0 - Disagree')
print('1 - Somewhat agree')
print('2 - Agree')
print()


def quiz():
    global selfpres, sexual, social, categories

    questions = [
        {"category": "wellbeing", "question": "I have a clear and conscious sense of how to take care of my health."},
        {"category": "wellbeing", "question": "I exercise regularly."},
        {"category": "wellbeing", "question": "I am aware of the kinds of foods that my body needs, and how to distinguish between unhealthy cravings and real nutrition. I am always looking for ways to help my body become better balanced."},
        {"category": "wellbeing", "question": "I avoid substances or activities that I feel will negatively impact my health."},
        {"category": "wellbeing", "question": "I notice when I am stressed, and take action to reduce my stress."},
        {"category": "wellbeing", "question": "I am attuned to my body's needs (eg. I know when I'm cold, when I'm thirsty, what foods support my health and well-being, and what environments are attuned to maximizing my energy. If I take supplements I know what supplements my body needs.)."},
        {"category": "wellbeing", "question": "My capacity for self-care feels good and often comes easily. I make time for self care."},
        {"category": "wellbeing", "question": "I adhere to routines/habits I need to maintain optimal health (eg. regular sleep, exercise, times to eat and what to eat, activities that help me maintain my health, brushing and flossing my teeth, skin care, etc.)."},
        {"category": "wellbeing", "question": "I notice the signs and symptoms of ill-health (be it stress, overwork, unhealthy foods, or whatever factors that are missing in my life that affect the health and well-being of my body) or impending illness and take appropriate action to take myself or get the care and attention I need."},
        {"category": "wellbeing", "question": "My physical state—amount of rest, overall health, energy level--profoundly impacts my sense of well-being as a whole."},
        {"category": "wellbeing", "question": "I often have my eye on the most recent health care innovations, and check all the angles on health and transformation, for example appropriate exercise, health tracking devices, supplements, medical innovations, latest medical research, acupuncture, chiropractic, naturopathic health, etc."},
        {"category": "resources", "question": "I have the ability, or awareness, to take care of my financial life."},
        {"category": "resources", "question": "I spend money wisely and manage my resources well so I can accumulate wealth, and track my spending and earning."},
        {"category": "resources", "question": "I secure and conserve the use of my resources. I'm aware of what I own (eg. money and posessions) and how to conserve and maximize those resources."},
        {"category": "resources", "question": "I am a practical person and I understand what it takes in the real world to expand and enhance my financial security and foundation because I understand how things work or am good at figuring out how to make things work. E.g., anything from how to invest money to finding new ways to make money, saving seeds, upcycling furniture, etc."},
        {"category": "resources", "question": "I track my budget and my earnings, so that I have certainty about my resources. Rather than guessing and hoping that I have enough for what I want to spend, I have real data that allows me to plan with certainty."},
        {"category": "resources",
              "question": "I am a resourceful person who is adaptable to changing circumstances, and enjoys learning and preparing for eventualities. E.g., power outages, having off-grid power supplies, securing alternative food resources."},
             {"category": "resources",
              "question": "I am efficient and like to use what I have. I have the ability to be frugal as needed so that I can make the most of what I have and avoid waste and unneccessary expenditures."},
             {"category": "resources",
              "question": "I like to be self-reliant; I don’t want to be affected by the chaos of others."},
             {"category": "resources",
              "question": "I am a good manager of my life. I create solid structures of consistency for maintaining my resources. This could be in areas such as time management, gardening, taking inventory of property and belongings, and money."},
             {"category": "resources",
              "question": "I am careful with my posessions. I know how to keep things from being damaged. I know how to fix stuff. I spot what is broken and go directly to the task of fixing it."},
             {"category": "home",
              "question": "I know how to create a cozy nest or home to abide in, I attend to domesticity, creating a safe haven where I can relax and settle in."},
             {"category": "home",
              "question": "I like comfort, stability, and familiarity in my routines, and my home environment supports my routines."},
             {"category": "home",
              "question": "I am aware of the nuances of my abode, E.g., temperature, cleanliness, organization, lighting, air quality, etc."},
             {"category": "home",
              "question": "I notice when things are disorganized or out of place and do somehting about it."},
             {"category": "home",
              "question": "I do things that make home a place of safety, comfort and support, i.e., their refrigerators are often well supplied with necessary food, they have back up plans for protecting their food support or energy supply, they’ve got comfortable furniture, etc."},
             {"category": "home",
              "question": "I possess the capacity to create a home environment that is sturdy, well cared for, and safe. I am conscious of the factors that contribute to this, and enjoy doing whatever it takes to create a sense of ‘home’ or home base."},
             {"category": "home",
              "question": "When I am in a space that feels chaotic or disorganized, I find it very unpleasant and difficult to ignore."},
             {"category": "home",
              "question": "Oganizing and bringing improvements to my space is a high leverage for my wellbeing. It brings me energy and joy and supports my whole life. Every improvement significantly raises my level of energy and inspiration!"},
             {"category": "home",
              "question": "I pay attention to aesthetics and organization, and enjoy learning new ways to bring beauty and order to the domestic sphere, such as getting design ideas, or learning about organizational techniques."},
             {"category": "home",
              "question": "When traveling, I tend to take a version of ‘home’ with me, creating a nest at the hotels or inns they stay in, bringing smaller versions of ‘home’ with me."},
            {"category": "evolutionary", 
     "question": "I am turned on by taking risks and seeking new adventures!"},
            {"category": "evolutionary", 
     "question": "I enjoy breaking up routines that are predictable."},
            {"category": "evolutionary", 
             "question": "Stability and comfort, while I enjoy them from time to time, tend to make me feel bored and restless."},
            {"category": "evolutionary", 
             "question": "I am an adventurous person. I like to explore the edges of life, to go into the unknown!"},
            {"category": "evolutionary", 
             "question": "I attune to what lights me up, turns me on, inspires me, and I go for it."},
            {"category": "evolutionary", 
             "question": "I am motivated by challenge. Bring it on! I love the challenges, and love tracking my excitement and what moves me, and love the intensity of tracking my passion (put simply: I love intensity! I love the zing!)"},
            {"category": "evolutionary", 
             "question": "I don’t hesitate to follow my passion, follow what juices me, and love the energy of encountering risk and unpredictability. I value the courage to push boundaries, and encourage others to grow and go beyond their comfort zones."},
            {"category": "evolutionary", 
             "question": "I learn to trust my attractions as profound guidance, giving me the guts to break patterns, to go to the depths of my soul, to listen to what truly makes my soul sing."},
            {"category": "evolutionary", 
             "question": "There's a part of me that feels aggressive, where I want to go for what attracts me energetically, be it an idea, a spiritual path, a book, an encounter with another human being, etc. This feeling gives me the guts and courage to show up for my passion."},
            {"category": "evolutionary", 
             "question": "I like the feeling of 'going for it!' I don't feel satisfied unless I've pushed my edges a bit."},
            {"category": "evolutionary", 
             "question": "I can't stand sitting back. When I see other people succeeding I feel competitive drive and either pain or inspiration to do something myself."},
            {"category": "broadcasting", 
             "question": "My light shines through and lights others up. I'm aware of my attractiveness to others."},
            {"category": "broadcasting", 
             "question": "I've been told I have natural charisma. My presence has a certain draw for people. I share my juiciness and charisma and broadcast this energy freely."},
            {"category": "broadcasting", 
             "question": "If someone isn't vibrant, it doesn't matter their appearance so much or what they are wearing, they don't look attractive to me."},
            {"category": "broadcasting", 
             "question": "When I'm feeling negative emotions, if I'm not mindful, I can impact the people around me strongly in a negative way. If I'm feeling good I light up the room."},
            {"category": "broadcasting", 
             "question": "I am looking for someone or something that is on my bandwidth of energy. I am aware of the magnetic field of the room, and attuned to those whose magnetism is even very strong. I seek out those magnetic interactions where there's a feel of chemistry, of aliveness. I pick up on those who are also lit up, and move towards them."}, 
            {"category": "broadcasting", "question": "I experience attraction and repulsion towards people clearly. This is the working of the broadcasting/attraction energy which I am registering/attuning with…I’m attracted to this person, place, book, idea, or…I’m repulsed by this person, place, book, idea, partner. I feel this in my body all day long!"},
            {"category": "broadcasting", "question": "I value feeling sexy and vibrant. I'm aware of my attractive features and how to bring them out. I enjoy tending to my appearance and grooming in order to enhance my attractiveness."},
            {"category": "broadcasting", "question": "I am always looking for that spark of energy between me and others, and particularly enjoy being the source of that spark."},
            {"category": "immersion", "question": "With the heart open, I can be completely immersed in someone and have no physical contact at all."},
            {"category": "immersion", "question": "Fully in contact with my body electric, the zing of my sexual/attraction energy, I open to the capacity for ecstasy."},
            {"category": "immersion", "question": "I have an intense, one-pointed focus and reflects my ability to deeply focus my attention, to zero in, to immerse myself in whatever has captured my attention."},
            {"category": "immersion", "question": "I prefer focus and intensity to a casual vibe."},    
            {"category": "immersion", "question": "I like to go deep in a subject, whether it's intellectual, emotional, or spiritual."},
            {"category": "immersion", "question": "I like it when people share their innermost experiences and things meaningful to them, and we can bond over those subjects."},
            {"category": "immersion", "question": "I have a strong urge to lose myself in something, whether it's a person, a book, a piece of music."},
            {"category": "immersion", "question": "When I put my attention on something, I'm not satisfied until I've reached a certain level of focus or depth. If I haven't been able to focus and explore with depth in an area during my day, I feel dissatisfied."},
            {"category": "immersion", "question": "I'm often not satisfied until I am able to reach a certain depth of understanding and really 'get' whatever I'm studying."},
            {"category": "immersion", "question": "I naturally gravitate towards deep exploration or discussion, and I enjoy learning environments where people are avidly studying and sharing knowledge and resources with each other."},
            {"category": "reading", "question": "I accurately interpret (via body, voice, facial expression, movement) what others are communicating."},
            {"category": "reading", "question": "I read between the lines and pick up on the nuances of people and what they are saying, overtly or covertly (I 'get' where they are coming from.)."},
            {"category": "reading", "question": "I know how to interpret others accurately. I can put myself in someone else's place and sense what they are communicating."},
            {"category": "reading", "question": "I can adapt to the needs of others, like a great parent."},
            {"category": "reading", "question": "I have the capacity to read whether others like me, or are interested in me, or whether they can be a true support for me, i.e., be an ally. That is—are they friend or foe?"},
            {"category": "reading", "question": "I can read the emotional temperature of the room. I can intuit what’s going on around me, can discern clearly what communications would work, and are able to notice how my communications land on others, and how they take it in."},
            {"category": "reading", "question": "I clearly notice the effect I have on others by my words, tone of voice, body language, and when something is either having a positive impact or rubbing others the wrong way."},
            {"category": "reading", "question": "When people are looking upset I wonder why other people don't pick up on these signals, or notice, when this seems obvious to me."},
            {"category": "reading", "question": "I intuitively attune to a group and to what will further communication and a sense of connection or teamwork."},
            {"category": "reading", "question": "I have the ability to learn and adapt new behaviors in my endeavor to work with others, I have confidence to interact and join the human family."},
            {"category": "bonding", "question": "I have the ability to co-create with others; I like to establish and build relationships with others even if I don’t like them necessarily."},
            {"category": "bonding", "question": "I can bond with others for the higher purpose of serving a goal together. I can create a bond that helps ‘us’ move towards a mutual goal."},
            {"category": "bonding", "question": "At my best, I create the feeling that everyone belongs, is a part of the team. I help people also to bond over a sense of the common needs and group purpose, and motivate them to act from that place."},
            {"category": "bonding", "question": "I have the skill and capacity to create mutual support with, and for, others so as to create win/win situations (I care about the team.)"},
            {"category": "bonding", "question": "I put principles before personalities, with kindness and grace. Eg., the importance of doing the right thing, seeing what would cause the least harm or regret, seeing the larger purpose beyond my own immediate needs, identity, or preferences."},
            {"category": "bonding", "question": "I naturally come by the art of staying connected with others, I inherently pick up on the social actions necessary for this, eg., sending emails to friends, recognizing birthdays and anniversaries or other life milestones with cards, etc."},
            {"category": "bonding", "question": "I can respond gracefully to the needs of others for the betterment of our mission together. I can give, adapt, and support others…and have the natural ability to see beyond myself and my own needs and perspectives to what would also speak to the people I want to connect with. Eg., making note of other peoples' particular preferences and needs."},
            {"category": "bonding", "question": "I generate warmth towards others that invites them to connect and work with me. Skilled also at sustaining connections with others, I know how to apply the social glue."},
            {"category": "bonding", "question": "I know how to develop reciprocity with others, to create teamwork and team spirit. I’m for you and you’re for me."},
            {"category": "bonding", "question": "I’m aware of what my connection with another person is (the state of my connection, is it good or bad), and how to facilitate building a better bond. Doesn’t mean I’m a social butterfly, or that I like groups, but that I have this skill and can apply it in areas that I value."},
            {"category": "contribution", "question": "I am passionate about contributing, helping and feeding the social good, and finding my particular mission to serve."},
            {"category": "contribution", "question": "I am aware of the unique gifts I have to contribute the best to others and I wish to give these to others. I am clear and confident in what I have to offer."},
            {"category": "contribution", "question": "I naturally see not only where I can serve, but where other people can share their gifts with the world. When I see others not sharing their gifts and being more exclusively focused on their own problems or wellbeing, it sometimes puzzles me why they don't seek out the natural avenues to contribute."},
            {"category": "contribution", "question": "I feel a part of the world and its troubles and feel an innate responsibility to help others. This shows up as being invested in the wellbeing of people around me and the community at large. I have a strong desire to contribute my gifts for the betterment of humanity. Eg., participating in charity, volunteer efforts, being involved in my community, keeping abreast of the issues that concern us as a whole, and finding a meaningful way within that to engage."},
            {"category": "contribution", "question": "I serve a meaningful purpose that connects me to the tribe of humanity. I know my calling, what I am here to serve, what my true and meaningful relationship with others is. I feel clear about how to match my own strengths and interests into something that would meaningfully benefit others. I contribute, I give away my gifts, while feeling a part of the good I am contributing to."},
            {"category": "contribution", "question": "I have the urge to engage. I have the capacity to participate in what is happening, to step in to life, to be a part of this life—to be a participant. (When people are weak in this social instinct sector it’s all about me, or I feel that I don’t have anything to offer)."},
            {"category": "contribution", "question": "I am aware more of the time than not that there are things that are more important than me and what I want—I see the needs of the greater whole and feel strongly motivated to act upon what I see."},
            {"category": "contribution", "question": "During the course of a day, I feel fulfilled and satisfied if I can be of service in a meaningful way to others, and somewhat empty if I haven't been able to do that."},
            {"category": "contribution", "question": "It pains me to see others' suffering. I have the urge to help alleviate others' suffering, and naturally see avenues to do that."},
            {"category": "contribution", "question": "I am always looking for ways I can have a positive impact on the people around me. I have the urge to help alleviate others' suffering, and naturally see avenues to do that."}
    ]
    
    categories = {"wellbeing": 0, "resources": 0, "home": 0, "evolutionary": 0, "broadcasting": 0, "immersion": 0, "reading": 0, "bonding":0, "contribution": 0}
    random.shuffle(questions)
    
    for question in questions:
        answer = int(input(question["question"] + " (0-2): "))
        categories[question["category"]] += answer
        print()

    selfpres = categories["wellbeing"] + categories["resources"] + categories["home"]
    sexual = categories["evolutionary"] + categories["broadcasting"] + categories["immersion"]
    social = categories["reading"] + categories["bonding"] + categories["contribution"]   

    return selfpres, sexual, social, categories


if __name__ == "__main__":
    quiz()

print("\nYour instinctual subtype scores:")
print(f'\nSubtype Self-Preservation: {selfpres}')
print("-----------------------------------")
print(f'Wellbeing: {categories["wellbeing"]}')
print(f'Resources/Practical Know How: {categories["resources"]}')
print(f'Home & Domesticity: Maintaining a Home: {categories["home"]}')
print(f'\nSubtype Sexual: {sexual}')
print("-----------------------------------")
print(f'Evolutionary Impulse: {categories["evolutionary"]}')
print(f'Broadcasting/Attraction: {categories["broadcasting"]}')
print(f'Immersion/Fusion: {categories["immersion"]}')
print(f'\nSubtype Social: {social}')
print("-----------------------------------")
print(f'Reading/Adapting: {categories["reading"]}')
print(f'Bonding/Affiliating: {categories["bonding"]}')
print(f'Contribution to others: {categories["contribution"]}')

print("\n")
print("\nAnalysis and Recommendations (may take a moment to generate)")
print("-----------------------------------")
print("\n")

   # load from disk
index = GPTSimpleVectorIndex.load_from_disk(
    "/Users/alexisneuhaus/Documents/Coding/GPTIndexFeb12/gpt_index/examples/paul_graham_essay/data2/index.json"
)

response = index.query(
    f"Based on the given scores for a person who is an Enneagram type {type} and took an Enneagram instinctual subtypes quiz and had scores of Subtype Self-Preservation: {selfpres} (subscores in that section were Wellbeing: {categories['wellbeing']}, Resources/Practical Know How: {categories['resources']}, Home & Domesticity: {categories['home']}), Subtype Sexual: {sexual} (subscores in that section were Evolutionary Impulse: {categories['evolutionary']}, Broadcasting/Attraction:{categories['broadcasting']}, Immersion/Fusion: {categories['immersion']}), and Subtype Social: {social} (subscores in that section were Reading/Adapting: {categories['reading']}, Bonding/Affiliating: {categories['bonding']}, Contribution to others: {categories['contribution']}), please provide analysis and recommendations for their growth."
)
print(response)
