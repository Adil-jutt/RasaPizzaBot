# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class SubmitOrderForm(Action):

	def name(self) -> Text:
		"""Unique identifier of the form"""
		return "submit_order_form"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
		
		global pizza_size 
		global pizza_amount 
		global pizza_type 
		pizza_size = tracker.get_slot("pizza_size")
		pizza_type = tracker.get_slot("pizza_type")
		pizza_amount = tracker.get_slot("pizza_amount")
		
		dispatcher.utter_message(text=f"Okay Great. Your order is {pizza_amount} {pizza_type} pizzas in {pizza_size}. Can you confirm please")
		return []

class SubmitDeliveryForm(Action):

	def name(self) -> Text:
		"""Unique identifier of the form"""
		return "submit_delivery_form"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
		
		name = tracker.get_slot("name")
		address = tracker.get_slot("address")
		phone = tracker.get_slot("phone")
		
		dispatcher.utter_message(text=f"---- YOUR ORDER ----- \n Pizza quantity: {pizza_amount} \n Pizza Type: {pizza_type} \n Pizza Size: {pizza_size}\n NAME: {name} \n ADDRESS: {address} \n PHONE: {phone} \n\n your order will be delivered soon. Thanks for ordering from 3H PIZZA")
		return []

class ActionChangeOrder(Action):
	def name(self):
		return 'action_change_order'

	def run(self, dispatcher, tracker, domain):
		pizza_size = tracker.get_slot("pizza_size")
		pizza_type = tracker.get_slot("pizza_type")
		pizza_amount = tracker.get_slot("pizza_amount")
		SlotSet("pizza_type", pizza_type)
		SlotSet("pizza_size", pizza_size)
		SlotSet("pizza_amount", pizza_amount)
		
		dispatcher.utter_message(text=f"Okay Great. Your order is {pizza_amount} {pizza_type} pizzas in {pizza_size}. Can you confirm please")
		return[]

class ActionPizzaOrderAdd(Action):
	def name(self):
		return 'action_pizza_order_add'

	def run(self, dispatcher, tracker, domain):
		pizza_size = tracker.get_slot("pizza_size")
		pizza_type = tracker.get_slot("pizza_type")
		pizza_amount = tracker.get_slot("pizza_amount")
		order_details =  str(pizza_amount + " "+pizza_type + " is of "+pizza_size )
		old_order = tracker.get_slot("total_order")
		return[SlotSet("total_order", [order_details]) if old_order is None else SlotSet("total_order", [old_order[0]+' and '+order_details])]

class ActionResetPizzaForm(Action):
	def name(self):
		return 'action_reset_pizza_form'

	def run(self, dispatcher, tracker, domain):

		return[SlotSet("pizza_type", None),SlotSet("pizza_size", None),SlotSet("pizza_amount", None)]


class ActionPizzaQuestions(Action):
	def name(self):
		return 'action_pizza_questions'


	def run(self, dispatcher, tracker, domain):
		
		return[]