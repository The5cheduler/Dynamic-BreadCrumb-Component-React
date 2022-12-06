
import React, { useState, useEffect} from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Breadcrumb from './components/Breadcrumb';



function App() {
  let path = window.location.pathname
  const api = "http://localhost:8000/"+ path
  // assign value of crumbs here
  const [currentBreadcrumbs, setcrumbs] = useState([])
  const [previousBreadcrumbs, setprevious] = useState([])

  useEffect(() => {
      const dataFetch = async() => {
      const response = await fetch(api)
      const data =  await response.json() 
      setcrumbs(data['childrenNodes'])
      setprevious(data['previousNodes'])
      
      }
      dataFetch();
  }, []);

  const selected = crumb => {
    const loadnewCrumbs = async() => {
    const response = await fetch(api+'/'+crumb)
    const bcrumbs = await response.json()
    }
}
   
  return (
    <div className="App container">
      <h2>Dynamic Breadcrumb Components </h2>
        <Breadcrumb currentBreadcrumbs = { currentBreadcrumbs } previousBreadcrumbs = {previousBreadcrumbs} selected = { selected } />
    </div>
  );
}

export default App;
