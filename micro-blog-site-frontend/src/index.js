import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Navbar from './components/navbar/Navbar';
import CardCarousel from './components/cardcarousel/CardCarousel';
import RichTextEditor from './components/richtexteditor/RichTextEditor'
import Comment from './components/comment/Comment';

ReactDOM.render(
  <React.StrictMode>
    <Navbar/>
    <RichTextEditor/>
    <CardCarousel/>
    <Comment/>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
