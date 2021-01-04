import React from 'react';
import axios from 'axios';

import { Card, Button } from 'antd';

import CustomForm from '../components/Form';

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

    handleDelete = (event) => {
        const prirodaID = this.props.match.params.prirodaID;
        axios.delete(`http://127.0.0.1:8000/api/${prirodaID}`);
        
        
        this.props.history.push('/');
        
    }

    render(){
        return(
            <div>
                <Card title={this.state.priroda.title}>
                    <p>{this.state.priroda.content}</p>
                </Card>

                <CustomForm
                    requestType="put"
                    prirodaID={this.props.match.params.prirodaID}
                    btnText = "Update"/>
                
                <form onSubmit={this.handleDelete} >
                    <Button type="danger" htmlType="submit">Delete</Button>
                </form>
            </div>
        )
    }
}

export default PrirodaDetail; 