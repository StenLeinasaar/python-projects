import quotes
import get_weather
import web_scraping
import datetime

class NewsLetter:

    def __init__(self):
        self.content = {'quote': {'include': True, 'content': quotes.get_quote() },
                        'weather': { 'include': True,'content': get_weather.get_forecast()},
                        'weblinks': { 'include': True, 'content': web_scraping.return_dictionary()}}
        self.recipents = ["sleinasa@skidmore.edu"]

        self.sender_credentials = {}

    def send_email(self):
        pass

    def format_message_html(self):
        html = f"""<html>
        <body>
            <main>
                <h1> Sten's Personal Newsletter - {datetime.date.today().strftime('%d %b %Y')}</h1>
        """


        # Formatting a daily quote
        if self.content['quote']['include']:
            html += f"""<h2>Quote of the day</h2>

                    <i>"{self.content['quote']['content']['quote']}</i> - {self.content["quote"]['content']['author']}
                    """

        
        #I will now format the web links

        if self.content['weblinks']['include']:

            html += """<div class="titleLinks">"""
            for element in self.content['weblinks']['content']:
                html += f"""

                <a href={self.content['weblinks']['content'][element]}><h3> {element} </h3></a>
                
            """

            html+= """ </div>
            """


        html += """ </main>
                </body>
            </html>
            """
        return html



if __name__ == '__main__':
    email = NewsLetter()
    with open('email.html', 'w', encoding ='utf-8') as file:
        file.write(email.format_message_html())
    
