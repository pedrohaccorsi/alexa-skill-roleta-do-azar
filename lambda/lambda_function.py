import os
import logging
import ask_sdk_core.utils as ask_utils
import random

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
        
        expected_rouletteName = handler_input.request_envelope.request.intent.slots["rouletteName" ].value 
        attr = handler_input.attributes_manager.persistent_attributes
        rouletteName = attr["name" ]
        items        = attr["items"]
        
        if ( rouletteName != expected_rouletteName ):
            return (
                handler_input.response_builder
                    .speak(f'Ops, não encontrei nenhuma roleta chamada {expected_rouletteName}!')
                    .response
            )
        
        if ( len(items) <= 1 ):
            return (
                handler_input.response_builder
                    .speak(f'Ops, a roleta possui somente {len(items)} ítens!')
                    .response
            )
             
        return (
            handler_input.response_builder
                .speak(self.__getLoser(items))
                .response
        )

    def __getLoser(self, items):

        chosen   = items[ random.randint(0, len(items)-1) ] 
        chosen_2 = ''
        chosen_3 = ''

        factor = random.randint(0, 20)
        for _ in range (factor):
            kind_of_response = random.randint(0, 16)  

        if ( kind_of_response == 0):
            chosen_2 = items[ random.randint(0, len(items)-1) ]
            while( chosen_2 == chosen ):
                chosen_2 = items[ random.randint(0, len(items)-1) ]
            return( f'O sortuto da vez é: {chosen} ... não, pensando bem, mudei de ideia... dessa vez é o {chosen_2}' )
            
        elif ( kind_of_response == 1):
            return ( f'O sortudo é o... , {chosen} !'  )

        elif ( kind_of_response == 2):
            return ( f'Com 53 por cento dos votos, ... , ... {chosen}, é você!' )

        elif ( kind_of_response == 3):
            return( f'A decisão é unânime: {chosen}' )

        elif ( kind_of_response == 4):
            return ( f'Nessa não preciso nem pensar, claro que é o {chosen}' )

        elif ( kind_of_response == 5 and len(items) >= 3 ):
            chosen_2 = items[ random.randint(0, len(items)-1) ]
            while( chosen_2 == chosen ): 
                chosen_2 = items[ random.randint(0, len(items)-1) ]
            chosen_3 = items[ random.randint(0, len(items)-1) ]
            while( chosen_3 == chosen or chosen_3 == chosen_2 ): 
                chosen_3 = items[ random.randint(0, len(items)-1) ]
            return ( f'Tô meio dividida entre {chosen} e {chosen_2}, na dúvida, vou de {chosen_3}' )

        elif ( kind_of_response == 6):
            chosen_2 = items[ random.randint(0, len(items)-1) ]
            while( chosen_2 == chosen ):
                chosen_2 = items[ random.randint(0, len(items)-1) ]
            return ( f'Par ou ímpar entre {chosen} e {chosen_2}' )

        elif ( kind_of_response == 7):
            return chosen

        elif ( kind_of_response == 8):
            chosen_2 = items[ random.randint(0, len(items)-1) ]
            while( chosen_2 == chosen ):
                chosen_2 = items[ random.randint(0, len(items)-1) ]
            return f'hmmm... se o ítem {chosen} foi sorteado alguma vez nos últimos 3 dias, então é {chosen_2}, mas se não, {chosen}'

        elif ( kind_of_response == 9):
            return ( f'O sortudo é o... , {chosen} !'  )

        elif ( kind_of_response == 10):
            return ( f'O ítem {chosen} tá meio suspeito, então vai ele mesmo' )

        elif ( kind_of_response == 11):
            return ( f'Pedi até pro google e ele acha que tem que ser o {chosen}' )

        elif ( kind_of_response == 12):
            chosen_2 = items[ random.randint(0, len(items)-1) ]
            while( chosen_2 == chosen ):
                chosen_2 = items[ random.randint(0, len(items)-1) ]
            return ( f'Eu eras mais {chosen}, mas pedi a opinião do pessoal aqui e aí me convenceram... {chosen_2}, é você' )

        elif ( kind_of_response == 13):
            return ( f'É muito difícil dizer isso, mas... infelizmente... acho que... quem volta pra casa hoje... é você ... , ... , ... , , , ... , , ... , {chosen}' )

        elif ( kind_of_response == 14):
            return ( f'haha {chosen}'  )

        elif ( kind_of_response == 15):
            return ( f'Juro que calculei 3 vezes e caiu {chosen} em todas' )

        else: 
            return'guga' if 'guga' in items else chosen 


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