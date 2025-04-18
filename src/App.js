import logo from './logo.svg';
import './App.css';
import HomePage from './components/home/HomePage';
import { Header, Footer } from './components/widjet/Header';
import { Route, Switch } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <Header logo="Это мой сайт" data='This is HomePage' />
      <Switch>
        <HomePage />
      </Switch>
      <Footer />
    </div>
  );
}

export default App;
