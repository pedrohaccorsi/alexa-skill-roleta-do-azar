import os
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder       import CustomSkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input       import HandlerInput
from ask_sdk_model                    import Response
from ask_sdk_s3.adapter               import S3Adapter

s3_adapter = S3Adapter(bucket_name=os.environ["S3_PERSISTENCE_BUCKET"])

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CriarRoletaIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ( 
            ask_utils.is_request_type("IntentRequest"    )(handler_input) and 
            ask_utils.is_intent_name( "CriarRoletaIntent")(handler_input) 
        )
               
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        slots              = handler_input.request_envelope.request.intent.slots
        rouletteName       = slots["rouletteName" ].value   
        items              = []
        
        if ( slots["itemOne"  ].value is not None ): items.append( slots["itemOne"  ].value )
        if ( slots["itemTwo"  ].value is not None ): items.append( slots["itemTwo"  ].value )
        if ( slots["itemThree"].value is not None ): items.append( slots["itemThree"].value )
        if ( slots["itemFour" ].value is not None ): items.append( slots["itemFour" ].value )
        if ( slots["itemFive" ].value is not None ): items.append( slots["itemFive" ].value )
        if ( slots["itemSix"  ].value is not None ): items.append( slots["itemSix"  ].value )

        outSpeach = f'Ok! Salvei a roleta {rouletteName} com os ítems '
        
        for i in range(len(items)):
            if i == len(items)-1:
                outSpeach += ' e ' + items[i]
            else:
                outSpeach += ' , ' + items[i]
                

        roulette_attributes = {
            "name": rouletteName,
            "items" : items
        }
        
        attributes_manager = handler_input.attributes_manager
        attributes_manager.persistent_attributes = roulette_attributes
        attributes_manager.save_persistent_attributes()
        
        return (
            handler_input.response_builder
                .speak(outSpeach)
                .response
        )


class RodarRoletaIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ( 
            ask_utils.is_request_type("IntentRequest"    )(handler_input) and 
            ask_utils.is_intent_name( "RodarRoletaIntent")(handler_input) 
        )
               
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        #attr = handler_input.attributes_manager.persistent_attributes
        #print(attr)
        
        chosen       = 'João' 
        rouletteName = handler_input.request_envelope.request.intent.slots["rouletteName" ].value 
        enrolation_0 = ' o sortudo da vez é...'
        enrolation_1 = ' hmmm...'
        enrolation_2 = ' ainda tô pensando pera...'
        enrolation_3 = ' o sortudo da vez é... ... ... ...'
        enrolation_4 = ' hhhhmmmmmmmmmmmmmmm... .... ...'
        enrolation_5 = ' ainda tô pensando, pera... ... ... ... ...'
        enrolation_6 = ' tá...'
        outSpeach    = (
            'Ok! Pra roleta ' +  
            rouletteName      +
            enrolation_0      + 
            enrolation_1      + 
            enrolation_2      + 
            enrolation_4      + 
            enrolation_5      + 
            enrolation_6      + 
            chosen
        )
        return (
            handler_input.response_builder
                .speak(outSpeach)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(persistence_adapter=s3_adapter)

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(RodarRoletaIntentHandler())
sb.add_request_handler(CriarRoletaIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()