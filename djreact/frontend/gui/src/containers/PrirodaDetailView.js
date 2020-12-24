import React from 'react';
import axios from 'axios';

import { Card } from 'antd';

class PrirodaDetail extends React.Component{

    state = {
        priroda: {}
    }

    componentDidMount() {
        const prirodaID = this.props.match.params.prirodaID;
        axios.get(`http://127.0.0.1:8000/api/${prirodaID}`)
            .then(res =>{
                this.setState({
                    priroda: res.data
                });
            })
    }

    render(){
        return(
            <Card title={this.state.priroda.title}>
                <p>{this.state.priroda.content}</p>
            </Card>
        )
    }
}

export default PrirodaDetail; 