import React from 'react';
import { Form, Input, Button, Spin } from 'antd';
import { LoadingOutlined } from '@ant-design/icons';
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';
import * as actions from '../store/actions/auth';

    const antIcon = <LoadingOutlined style={{ fontSize: 24 }} spin />;

    

class NormalLoginForm extends React.Component {

    // handleSubmit = (e) => {
    //     e.preventDefault();
    //     // this.props.form.validateFields((err, values) => {
    //     //     if (!err) {
    //     //         console.log('Received values of form: ', values);
    //     //     }
    //     // });
    // }

    onFinish = values => {
        console.log('Success:', values);

        this.props.onAuth(values.username, values.password);

        this.props.history.push('/');
    };

    onFinishFailed = errorInfo => {
        console.log('Failed:', errorInfo);
    };

    render() {

        let errorMessage = null;

        if (this.props.error) {
            errorMessage = (
                <p>{this.props.error.message}</p>
            );
        }

        return (
            <div>
                {errorMessage}
                {
                    this.props.loading ?

                    <Spin indicator={antIcon} />

                    :

                    //onSubmitCapture={(event) => this.handleSubmit(event)}
                
                    <Form  name="basic" initialValues={{ remember: true }} onFinish={this.onFinish}  onFinishFailed={this.onFinishFailed}  className="login-form">


                        <Form.Item label="Username" name="username"
                                rules={[
                                {
                                    required: true,
                                    message: 'Please input your username!',
                                },
                                ]}
                            >
                            <Input />
                        </Form.Item>

                        <Form.Item label="Password" name="password"
                            rules={[
                            {
                                required: true,
                                message: 'Please input your password!',
                            },
                            ]}
                        >
                            <Input.Password />
                        </Form.Item>

                        <Form.Item>
                            <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
                                Login
                            </Button>
                            Or  <NavLink style={{marginRight: '10px'}} to='/signup/'>
                                Signup    
                            </NavLink>
                        </Form.Item>
                        
                    </Form>
                }
            </div>
        );
    }
}

// const WrappedNormalLoginForm = Form.create({})(NormalLoginForm);

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, password) =>  dispatch(actions.authLogin(username, password)) 
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(NormalLoginForm);
