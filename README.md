# chat-bot

This is a full stack chat bot application like chat GPT with enhanced capability to give you results based on read time data. You can ask current affairs questions along with the general question. It has also in built memory.

## How to run the application:

First, clone the repository

```
git clone https://github.com/asifrahaman13/chat-bot.git
```
Next, open the terminal and enter into the backend folder. 

```
cd backend/
```
Next, create a virtual environment. 

```
virualenv venv
```

Activate the  virtual environment. The following code works for UNIX based system( Linux and Max OS)

```
source venv/bin/activate
```

Install all the dependencies.

```
pip install -r requirements.txt
```
Next, run the backend server.

```
uvicorn main:app --reload
```
Now in another terminal open the front end.

```
cd frontend/
```

Install the dependencies

```
yarn install
```

Start your development server

```
yarn start
```

## MIT License

Copyright (c) 2023 Asif Rahaman
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
