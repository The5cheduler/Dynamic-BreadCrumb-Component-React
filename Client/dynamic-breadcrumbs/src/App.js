import logo from './logo.svg';
import React, { useState, useEffect} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Breadcrumb from './components/Breadcrumb';


function App() {

   // assign value of crumbs here
   const [data, setdata] = useState([]); 
   const [crumbs, setcrumbs] = useState([]); 

  const fetchdata = async() => {
    const response = await fetch("http://localhost:8000/path")
    const data = await response.json()
    setdata(data.data);
    
  }

 

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
