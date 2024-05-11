import google.generativeai as genai


def generate_itinerary(num_persons,destination,num_days,preferences):
    genai.configure(api_key="<API-KEY>")
    model = genai.GenerativeModel('gemini-pro')

    prompt = f"""Generate a customized {num_days}-day itinerary for {num_persons} traveler(s) in {destination}, incorporating their interests in {preferences}.

    Itinerary Guidelines:

    1. Variety and Coverage: Each day should offer unique experiences, ensuring all traveler preferences are addressed throughout the itinerary.
    2. Balance: Avoid overloading any day with excessive activities. Prioritize a relaxed and enjoyable pace.
    3. Focus on Preferences: Tailor the itinerary solely to the provided preferences. Don't introduce any extraneous suggestions.
    4. Additional Tips: Include helpful recommendations beyond the daily itinerary to enhance the traveler's experience.

    Output Format:
    DAY 1:
    -> Take a day trip to the Ajanta and Ellora Caves (UNESCO World Heritage Site)
    -> Visit the Mani Bhavan Gandhi Museum
    -> Go shopping at Linking Road 
    -> Take a walk through the Chor Bazaar 
    .
    .
    .
    DAY N:

    -> Visit the Haji Ali Dargah 
    -> Go shopping at Crawford Market
    -> Visit the Gateway of India 
    -> Enjoy the nightlife at Kamala Mills 

    """

    generated_itinerary = model.generate_content(prompt)
    return generated_itinerary.text