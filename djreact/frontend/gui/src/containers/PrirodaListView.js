import React from 'react';
import axios from 'axios';

import Prirodas from '../components/Priroda'

class PrirodaList extends React.Component{

    state = {
        prirodas: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/')
            .then(res =>{
                this.setState({
                    prirodas: res.data
                });
            })
    }

    render(){
        return(
            <Prirodas data={this.state.prirodas} />
        )
    }
}

export default PrirodaList; 