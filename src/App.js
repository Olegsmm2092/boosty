import logo from './logo.svg';
import './App.css';
import HomePage from './components/home/HomePage';
import AboutPage from './components/about/AboutPage';
import { Header, Footer } from './components/widjet/Header';
import { Route, Switch } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <Header logo="Это мой сайт" data='This is HomePage' />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/about" component={AboutPage} />
        <HomePage />
      </Switch>
      <Footer />
    </div>
  );
}

export default App;
