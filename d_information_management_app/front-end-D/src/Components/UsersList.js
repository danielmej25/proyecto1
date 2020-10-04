import React, { Component } from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '../css/sb-admin-2.css'
import '../css/sb-admin-2.min.css'
import '../vendor/fontawesome-free/css/all.min.css'
import '../js/validarForm'

import  UsuariosService  from  './UsuariosService';
const  usuariosService  =  new  UsuariosService();



class UsersList extends Component {
    constructor(props){
        super(props);
        this.state = {
            usuarios: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    componentDidMount() {
        var  self  =  this;
        usuariosService.getUsuarios().then(function (result) {
            self.setState({ usuarios:  result.data, nextPageURL:  result.nextlink})
        });
    }
    handleDelete(e,pk){
        var  self  =  this;
        usuariosService.deleteUsuario({pk :  pk}).then(()=>{
            var  newArr  =  self.state.usuarios.filter(function(obj) {
                return  obj.pk  !==  pk;
            });
            self.setState({usuarios:  newArr})
        });
    }
    nextPage(){
        var  self  =  this;
        usuariosService.getUsuariosByURL(this.state.nextPageURL).then((result) => {
            self.setState({ usuarios:  result.data, nextPageURL:  result.nextlink})
        })};
        render() {
        
            return (
            <div  className="usuarios--list">
                <table  className="table">
                    <thead  key="thead">
                    <tr>
                        <th>#</th>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                        {this.state.usuarios.map( u  =>
                        <tr  key={u.pk}>
                            <td>{u.pk}  </td>
                            <td>{u.username}</td>
                            <td>{u.email}</td>
                            <td>
                            <button  onClick={(e)=>  this.handleDelete(e,u.pk) }> Delete</button>
                            <a  href={"/usuario/" + u.pk}> Update</a>
                            </td>
                        </tr>)}
                    </tbody>
                </table>
                <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
            </div>
            );
        }


}

export default UsersList;