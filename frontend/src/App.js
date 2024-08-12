import './App.css';
import SavingGoalAdd from './components/SavingGoalAdd.js';
import SavingGoals from './components/SavingGoals.js';
import AuthorizationForm from './components/AuthorizationForm.js';
import RegistrationForm from './components/RegistrationForm.js';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/reg" element={<RegistrationForm />} />
        <Route path="/log" element={<AuthorizationForm />} />
        <Route path="/goals" element={<SavingGoals />} />
        <Route path="/goal-form" element={<SavingGoalAdd />} />
      </Routes>
    </div>
  );
}

export default App;
