import logo from './logo.svg';
import './App.css';
import HomePage from './components/home/HomePage';
import AboutPage from './components/about/AboutPage';
import { Header, Footer } from './components/widjet/Header';
import { Route, Routes } from 'react-router-dom';

function NotFound() {
  return (<h1>Not Found</h1>);
}

function App() {
  return (
    <div className="App">
      <Header logo="Это мой сайт" data='This is HomePage' />
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/about" element={<AboutPage/>} />
        <Route path="*" element={<NotFound/>} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
