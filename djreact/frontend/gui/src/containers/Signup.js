import React from 'react';
import {
  Form,
  Input,
  Button
} from 'antd';
import { NavLink } from 'react-router-dom';
import * as actions from '../store/actions/auth';
import { connect } from 'react-redux';

class RegistrationForm extends React.Component {



   onFinish = (values) => {
    console.log('Received values of form: ', values);

    this.props.onAuth(values.username, values.email, values.password, values.confirm);

    this.props.history.push('/');
  };

    render() {

            return (
                <div>

                    <Form
                    
                    name="register"
                    onFinish={this.onFinish}

                    scrollToFirstError
                    >

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

                    <Form.Item
                        name="email"
                        label="E-mail"
                        rules={[
                        {
                            type: 'email',
                            message: 'The input is not valid E-mail!',
                        },
                        {
                            required: true,
                            message: 'Please input your E-mail!',
                        },
                        ]}
                    >
                        <Input />
                    </Form.Item>

                    <Form.Item
                        name="password"
                        label="Password"
                        rules={[
                        {
                            required: true,
                            message: 'Please input your password!',
                        },
                        ]}
                        hasFeedback
                    >
                        <Input.Password />
                    </Form.Item>

                    <Form.Item
                        name="confirm"
                        label="Confirm Password"
                        dependencies={['password']}
                        hasFeedback
                        rules={[
                        {
                            required: true,
                            message: 'Please confirm your password!',
                        },
                        ({ getFieldValue }) => ({
                            validator(rule, value) {
                            if (!value || getFieldValue('password') === value) {
                                return Promise.resolve();
                            }

                            return Promise.reject('The two passwords that you entered do not match!');
                            },
                        }),
                        ]}
                    >
                        <Input.Password />
                    </Form.Item>

                    <Form.Item>
                            <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
                                                Signup
                            </Button>
                            Or  <NavLink style={{marginRight: '10px'}} to='/login/'>
                                                Login    
                            </NavLink>
                    </Form.Item>

                    </Form>

                </div>

            );
    }
}

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, email, password, confirm) =>  dispatch(actions.authSignup(username, email, password, confirm)) 
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(RegistrationForm);
