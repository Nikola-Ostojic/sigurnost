import React from 'react';
import { Form, Input, Button } from 'antd';

// const FormItem = Form.Item;

class CustomForm extends React.Component{ 

    // constructor() {
    //     super();

    //     this.title = "";
    //     this.content = "";

    //     this.handleClick = this.handleClick.bind(this);
    //     this.handleFormSubmit = this.handleFormSubmit.bind(this);
    //   }

    handleFormSubmit = (event) => {
        event.preventDefault();
        const title = event.target.elements.title.value;
        const content = event.target.elements.content.value;

        console.log(title, content);
    }

    // handleClick(event) {
    //     const title = event.target.elements.title.value;
    //     const content = event.target.elements.content.value;

    //     console.log(title, content);
    // }

    render(){
        return(
            <div>
                <Form onSubmitCapture = {this.handleFormSubmit}>
                    <Form.Item label = "Title">
                        <Input name="title" ref={node => (this.tittle = node)} id="title" placeholder="Put a title here" />
                    </Form.Item>
                    <Form.Item label = "Content">
                        <Input name="content" ref={node => (this.conntent = node)} placeholder="Enter some content here" />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType = "submit" >Submit</Button>
                    </Form.Item>                                       
                </Form>
            </div>
        );
    }
}

export default CustomForm;


