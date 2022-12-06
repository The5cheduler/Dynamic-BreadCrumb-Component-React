import logo from './logo.svg';
import React, { useState, useEffect} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Breadcrumb from './components/Breadcrumb';


function App() {

  const fetchcrumbs = async() => {
    const response = await fetch("http://localhost:8000/todo")
  }

  // assign value of crumbs here
  const [crumbs, setcrumbs] = useState(["home", "myname"]); 

  const selected = crumb => {
    console.log(crumb)
  }

  return (
    <div className="App container">
      <Breadcrumb crumbs = { crumbs } selected = { selected }/>
    </div>
  );
}

export default App;
