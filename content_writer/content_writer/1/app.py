import os
import sys
import json
import input_types

base_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(base_dir, "0.Refined_Business_idea", "RBI"))
sys.path.append(os.path.join(base_dir, "1.Business_Analyst", "BA"))
sys.path.append(os.path.join(base_dir, "2.Marketing_Strategy", "MS"))
sys.path.append(os.path.join(base_dir, "3.Policies", "P"))
sys.path.append(os.path.join(base_dir, "4.Break_Down_Info", "BDI"))
sys.path.append(os.path.join(base_dir, "5.Branding", "SM", "SM"))



from app import refined_business_idea
from BA import budget_maker
from MS import marketing_strategy
from P import business_policies
from BDI import break_down_info
from SM import slogan_maker


output_dir = './docs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def business_model_generator(userInput: input_types.userInput):
    # The following function will call the function of generating individual items
    print(userInput)
    print("Refining Business...")
    rfnd_bsns_idea = refined_business_idea(userInput)
    print("Making Budget...")
    budget = budget_maker(userInput, rfnd_bsns_idea)
    print("Making Marketing Strategy...")
    mrktng_strtgy = marketing_strategy(userInput, rfnd_bsns_idea, budget)
    print("Developing Policies...")
    bsns_plicies = business_policies(userInput, rfnd_bsns_idea)
    print("Branding...")
    branding = break_down_info(userInput, rfnd_bsns_idea, mrktng_strtgy)
    print("Slogans...")
    slogan = slogan_maker(userInput, branding)
    result = {
        "refined_business_idea": rfnd_bsns_idea,
        "budget": budget,
        "marketing_strategy": mrktng_strtgy,
        "business_policies": bsns_plicies,
        "branding": branding,
        "slogan": slogan,
    }
    try:
        result_file_path = os.path.join(base_dir, "result.JSON")
        with open(result_file_path, "w") as outfile:
            json.dump(result, outfile)

            # outfile.write("# Business Plan Results\n\n")

            # outfile.write("## Refined Business Idea\n")
            # outfile.write(f"{result['refined_business_idea']}\n\n")

            # outfile.write("## Budget\n")
            # outfile.write(f"{result['budget']}\n\n")

            # outfile.write("## Marketing Strategy\n")
            # outfile.write(f"{result['marketing_strategy']}\n\n")

            # outfile.write("## Business Policies\n")
            # outfile.write(f"{result['business_policies']}\n\n")

            # outfile.write("## Branding\n")
            # outfile.write(f"{result['branding']}\n\n")

        print("Results written to result.md successfully!")
    except FileNotFoundError:
        print("Error")
    print(result)
    return result


def piplineBegins(
    input_name: str = "OEnergy",
    input_location: str = "Global",
    input_business_idea: str = "A global research institue which will deal on the new technologies in energy production. We will also sale our latest solutions to different power companies. Vision is to build a dyson sphere in 50 years.",
):
    # input_name = input("Enter the name of your Business: ")
    # input_location = input("Enter the target location: ")
    # input_business_idea = input("Enter the business idea: ")

    userInput = {
        "name": input_name,
        "location": input_location,
        "plan": input_business_idea,
    }
    final_result = business_model_generator(userInput=userInput)
    return final_result


piplineBegins()
