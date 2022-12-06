
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

  const selected = (crumb,ci) => {
    let clickedDestination = '/'
    let inpreviousLevel = false ;
    let incurrentLevel = false ;
    inpreviousLevel = previousBreadcrumbs.includes(crumb)
    incurrentLevel = currentBreadcrumbs.includes(crumb)
    
    if (inpreviousLevel === true) {
      let temp = ''
      for(let i = 0; i <= ci ; i++) 
      {
        temp = temp + '/' + previousBreadcrumbs[i]
      }
      window.location.href = `${temp}`
      
    }
    if (incurrentLevel === true) {
      let temp = ''
      for(let i = 0; i < previousBreadcrumbs.length ; i++) 
      {
        temp = temp + '/' + previousBreadcrumbs[i]
      }
      for (let i = 0; i <= ci ; i ++){
        if(!currentBreadcrumbs[i].includes('.')){
        temp = temp + '/' + currentBreadcrumbs[i]
        }
      }
      window.location.href = `${temp}`
    }
    }


  // window.location.href = `${crumb}`

   
  return (
    <div className="App container">
      <h2>Dynamic Breadcrumb Components </h2>
        <Breadcrumb currentBreadcrumbs = { currentBreadcrumbs } previousBreadcrumbs = {previousBreadcrumbs} selected = { selected } />
    </div>
  );
}

export default App;
