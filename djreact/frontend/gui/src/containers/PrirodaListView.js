import React from 'react';
import axios from 'axios';

import Prirodas from '../components/Priroda'
import CustomForm from '../components/Form';

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
            <div>
                <Prirodas data={this.state.prirodas} />
                <br />
                <h2>Create an article</h2>
                <CustomForm
                    requestType="post"
                    prirodaID={null}
                    btnText="Create"/>
            </div>
        )
    }
}

export default PrirodaList; 