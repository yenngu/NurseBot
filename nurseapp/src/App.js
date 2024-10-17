import './App.css';

function App() {
  return (
    <>
      <div class="top-section">
        <h1> Nurse Bot</h1>
      </div>

      <div class="result-container">
        <textarea readOnly>

        </textarea>
      </div>
      <div class="user-container">
        <input></input>
        <button className="submit-button"> Ask Bot... </button>
      </div>
    </>
  );
}

export default App;