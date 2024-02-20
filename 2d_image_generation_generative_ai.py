import openai
import requests

# Put your OpenAI API key here
openai.api_key = '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'

def generate_image_from_text_openai(text_description, output_path):
    openai.api_key = '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'

    try:
        response = openai.Image.create(
            prompt=text_description,
            n=1,
            size="1024x1024"
        )

        # Assuming the response contains a URL to the image
        image_url = response['data'][0]['url']

        # Download the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(image_response.content)
            print(f"Image saved to {output_path}")
        else:
            print("Failed to download the image.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
text_description = "Give me the image for the car standing in desert"
output_path = "generated_image.png"
generate_image_from_text_openai(text_description, output_path)
