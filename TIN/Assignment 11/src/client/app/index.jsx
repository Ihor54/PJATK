import React from 'react';
import {render} from 'react-dom';
import FirstForm from './FormComponent.jsx';

class App extends React.Component{
    render(){
        return (
          <div> 
              <FirstForm></FirstForm>
          </div>  
        );
    }
}

render(<App/>, document.getElementById('app'));