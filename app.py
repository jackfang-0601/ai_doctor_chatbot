from flask import Flask, render_template, request, jsonify, session
import uuid
from hello import DoctorConversation

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Add a secret key for session management

conversations = {}

@app.route('/')
def index():
    # Generate a new session ID for each new visitor
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    country = request.form.get('country', '').strip()
    user_id = session.get('user_id')
    
    # Create a unique conversation ID combining user_id and timestamp
    conversation_id = f"{user_id}_{uuid.uuid4()}"
    
    try:
        convo = DoctorConversation(country)
        conversations[conversation_id] = convo
        session['current_conversation'] = conversation_id
        return jsonify({'status': 'ok', 'message': 'Conversation started.'})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    conversation_id = session.get('current_conversation')
    user_input = request.form.get('message', '').strip()
    
    convo = conversations.get(conversation_id)
    if not convo:
        return jsonify({'status': 'error', 'message': 'Conversation not started.'})

    convo.messages.append({'role': 'user', 'content': user_input})

    response = convo.client.chat.completions.create(
        model='gpt-4o-mini',
        messages=convo.messages,
        temperature=1
    )
    reply = response.choices[0].message.content
    convo.messages.append({'role': 'assistant', 'content': reply})

    finished = any(x in reply for x in ['Here is a summary', 'Summary for your real doctor', 'SUMMARY FOR DOCTOR', 'SYMPTOMS:', 'ASSESSMENT:', 'RECOMMENDATIONS:'])

    return jsonify({'status': 'ok', 'reply': reply, 'finished': finished})

# Add a new endpoint to explicitly start a new conversation
@app.route('/new_conversation', methods=['POST'])
def new_conversation():
    # Clear the current conversation from session
    if 'current_conversation' in session:
        del session['current_conversation']
    return jsonify({'status': 'ok', 'message': 'Ready for new conversation.'})

if __name__ == '__main__':
    app.run(debug=True)
