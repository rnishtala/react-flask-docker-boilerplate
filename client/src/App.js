import React, { Component } from 'react';
import './App.css';
import Results from './components/Results';
import NewName from './components/NewName';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      names: [],
      loading: true
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    console.log(event.target.value)
    this.setState({ name: event.target.value });
  }

  async handleSubmit(event) {
    event.preventDefault();
    this.setState({
      loading: true,
    })
    console.log("===================")
    console.log(this.state.name)
    await fetch('http://localhost:5000/addname/' + this.state.name, {
      method: 'GET'
    });
    this.getNames()
  }

  getNames() {
    fetch('http://localhost:5000/getnames/')
      .then(response => response.json())
      .then(json => {
        this.setState({
          name: '',
          names: json,
          loading: false
        })
      })
  }

  componentDidMount() {
    this.getNames();
  }

  render() {
   return (
     <div className="App">
       <header className="App-header">
         <NewName handleChange={this.handleChange} handleSubmit={this.handleSubmit} value={this.state.name} />
         {this.state.loading ? <h1>Loading</h1> : <Results {...this.state} />}
       </header>
     </div>
   );
 }
}


export default App;
