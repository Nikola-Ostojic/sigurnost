import React from 'react';
import { Form, Input, Button } from 'antd';

import axios from 'axios';

class CustomForm extends React.Component{ 

    handleFormSubmit = (event, requestType, prirodaID) => {
        const title = event.target.elements.title.value;
        const content = event.target.elements.content.value;
        
        // eslint-disable-next-line default-case
        switch (requestType) {
            case 'post':
                return axios.post('http://127.0.0.1:8000/api/', {
                    title: title,
                    content: content
                })
                .then(res => console.log(res), window.location.reload())
                .catch(error => console.err(error));
            case 'put':
                return axios.put(`http://127.0.0.1:8000/api/${prirodaID}/`, {
                    title: title,
                    content: content
                })
                .then(res => console.log(res), window.location.reload())
                .catch(error => console.err(error));
        }
    }

    render(){
        return(
            <div>
                <Form onSubmitCapture = {(event) => this.handleFormSubmit(
                    event,
                    this.props.requestType,
                    this.props.prirodaID
                )}>
                    <Form.Item label = "Title">
                        <Input name="title" ref={node => (this.tittle = node)} id="title" placeholder="Put a title here" />
                    </Form.Item>
                    <Form.Item label = "Content">
                        <Input name="content" ref={node => (this.conntent = node)} placeholder="Enter some content here" />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType = "submit" >{this.props.btnText}</Button>
                    </Form.Item>                                       
                </Form>
            </div>
        );
    }
}

export default CustomForm;


