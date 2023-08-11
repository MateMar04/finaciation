import React from "react";
import '../assets/styles/RowWithCheck.css'
import Check from "../assets/images/checked.gif";
import {Link} from "react-router-dom";
import {Button, Col, Container, Modal, Row} from "react-bootstrap";


export const SucceedModal = (props, {message}) => {
    return (
        <Modal show={props.show}>
            <Modal.Body>
                <Container className='justify-content-center'>
                    <Row className='justify-content-center'>
                        <Col lg={5}>
                            <img src={Check} alt="CheckButton" className="mx-auto img-fluid"/>
                            <p className="text-center">¡Se a registrado {message} correctamente!</p>
                        </Col>
                    </Row>
                </Container>
            </Modal.Body>
            <Modal.Footer>
                <Link to={'/login'}>
                    <Button onClick={props.onClose} variant="success">
                        OK
                    </Button>
                </Link>
            </Modal.Footer>
        </Modal>
    )
}

export default SucceedModal