import React, { useState, useEffect } from 'react';
import axios from 'axios';

function SavingGoals() {
  const [goals, setGoals] = useState([]);
  useEffect(() => {
    axios
      .get('http://localhost:8000/saving_goals/')
      .then(response => setGoals(response.data))
      .catch(error => console.error('Ошибка при получении данных:', error));
  }, []);

  return (
    <>
      <h1>Цели сбережения</h1>
      {goals.map(goal => (
        <div key={goal.id}>
          <h2>{goal.title}</h2>
        </div>
      ))}
    </>
  );
}

export default SavingGoals;
