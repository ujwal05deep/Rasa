# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class Searchcountry(Action):

    def name(self) -> Text:
        return "action_search_country"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        message = 'No country mentioned'
        for e in entities: 
            if e['entity'] == 'country':
                country = e['value']
                if country == 'India':
                     message = 'https://www.holidify.com/country/india/places-to-visit.html'
                                
                elif country =='America':
                    message = 'https://www.holidify.com/country/usa/places-to-visit.html'
                elif country =='France':
                    message = 'https://www.holidify.com/country/france/places-to-visit.html'
                elif country=='England' :
                    message = 'https://www.holidify.com/country/england/places-to-visit.html'
                else :
                    message ='No country with this name'

        dispatcher.utter_message(text=message)

        return []
    

class HotelBokking(Action):

    def name(self) -> Text:
        return "action_return_hotel_flight_booking"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg="https://www.goibibo.com/"
        dispatcher.utter_message(text=msg)

        return []
    
class Attraction(Action):

    def name(self) -> Text:
        return "action_return_attraction"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        message = 'Please select proper country'
        for e in entities: 
            if e['entity'] == 'country':
                country = e['value']
                if country == 'India':
                     message = 'https://www.holidify.com/collections/tourist-attractions-in-india'
                                
                elif country =='America':
                    message = 'https://www.planetware.com/tourist-attractions/usa-us.htm'
                elif country =='France':
                    message = 'https://www.planetware.com/tourist-attractions/france-f.htm'
                elif country=='England' :
                    message = 'https://www.planetware.com/tourist-attractions/england-eng.htm'
                else :
                    message ='No country with this name'

        dispatcher.utter_message(text=message)

        return []    

