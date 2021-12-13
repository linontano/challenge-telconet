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
    //API
  }
  checkIp = (ipNumber) =>{
    if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipNumber))
    {
      return (true)
    }
    alert("You have entered an invalid IP address!")
    return (false)
  }
  componentDidUpdate(){
    const BASE = "https://jsonplaceholder.typicode.com/todos";
    if(this.state.isLoaded){
      console.log("Checking DATA!", BASE)
      fetch(BASE)
        .then(response=>response.json())
        .then(json => {this.setState({ output: json, isLoaded: false })})
    }
  }
  render() {
    const { output, ip } = this.state
    return(
      <React.Fragment>
        <NavBar />
        <main className="container mx-auto">
          <FormInput 
            onChange={this.handleChange}
            onSubmit={this.handleSubmit}
            input={ip}
            />
            {
              output.length > 0 ?
              output.map((item, index)=>(
                <p key={index}>{ item.title }</p>
              ))
              :
              <p className="text-center">No existen elementos que mostrar</p>
            }
            
        </main>
      </React.Fragment>
    )
  }
}
 

export default App;
