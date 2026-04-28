import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function 
from prompts import system_prompt
from config import MAX_ITERS

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    parser = argparse.ArgumentParser(description="Wafflehaus")
    parser.add_argument("user_prompt", type=str, help="Please insert a prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(MAX_ITERS):
        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")

    print(f"Maximum interations ({MAX_ITERS}) reached") 
    sys.exit(1)
    


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = messages,
        config = types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction = system_prompt,
            temperature= 0
        )
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
   
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    if not response.function_calls:
        return response.text

    function_call_result_response_lst = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)

        if function_call_result.parts == None:
            raise ValueError("function_call_results.parts has returned with None (no parts)")

        if function_call_result.parts[0].function_response == None:
            raise ValueError ("function_call_results.parts[0].function_response has returned with None (no value)")

        if function_call_result.parts[0].function_response.response == None:
            raise ValueError ("function_call_results.parts[0].function_response.response has returned with None (no value)")

        function_call_result_response_lst.append(function_call_result.parts[0])

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

    messages.append(types.Content(role="user", parts=function_call_result_response_lst))
    
if __name__ == "__main__":
    main()

