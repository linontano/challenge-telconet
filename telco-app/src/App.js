import React, { Component } from 'react';
import NavBar from './components/navbar'
import FormInput from './components/formInput';


class App extends Component{
  constructor(props){
    super(props);
    this.state = {
      ip: "",
      output: [],
      isLoaded: false
    }
  }
  handleChange = (event) => {
    this.setState({ip:event.target.value})
  };
  handleSubmit = (event) => {
    this.setState({ isLoaded: true })
    event.preventDefault();
  }
  componentDidUpdate(){
    if(this.state.isLoaded){
      const BASE = "http://backend:5000/api/routes/"+this.state.ip;
      console.log("Checking DATA!", BASE)
      fetch(BASE)
        .then(response=>response.json())
        .then(json => {this.setState({ output: json, isLoaded: false })})
    }
  }
  render() {
    const { output, ip } = this.state
    console.log(output);
    return(
      <React.Fragment>
        <NavBar />
        <main className="container mx-auto">
          <FormInput 
            onChange={this.handleChange}
            onSubmit={this.handleSubmit}
            input={ip}
            />
            <div className="p-2">
            {
              Object.entries(output).length > 0 ?
              
                <pre>{ output["OUTPUT"] ?? output.message }</pre>
              
              :
              <p className="text-center">No existen elementos que mostrar</p>
            }
            </div>
            
        </main>
      </React.Fragment>
    )
  }
}
 

export default App;
