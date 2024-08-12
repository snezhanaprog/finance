import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import SavingGoalAdd from './SavingGoalAdd.js';
import SavingGoals from './SavingGoals.js';
import AuthorizationForm from './AuthorizationForm.js';
import RegistrationForm from './RegistrationForm.js';

function RouterApp() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/reg">регистрация</Link>
            </li>
            <li>
              <Link to="/log">авторизация</Link>
            </li>
            <li>
              <Link to="/goals">цели сбережения</Link>
            </li>
            <li>
              <Link to="/goals-form">форма цели</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/reg">
            <RegistrationForm />
          </Route>
          <Route path="/log">
            <AuthorizationForm />
          </Route>
          <Route path="/goals">
            <SavingGoals />
          </Route>
          <Route path="/goals-form">
            <SavingGoalAdd />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default RouterApp;
