import React, {useState} from 'react'
import './App.css';

function App() {

  const [userInput, setUserInput] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async() => {
    const res = await fetch('http://localhost:5000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify ({message: userInput}),
    });

    const data =await res.json();
    setResponse(data.response);
  }

  return (
    <>
      <div class="top-section">
        <h1> Nurse Bot</h1>
      </div>

      <div class="result-container">
        <textarea readOnly placeholder="Nurse Bot Will Answer Here..." value={response}>

        </textarea>
      </div>
      <div class="user-container">
        <input 
          value = {userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Ask NurseBot a Question..."
        />
        <button className="submit-button" onClick={handleSubmit}> Ask Question </button>
      </div>
    </>
  );
}

export default App;