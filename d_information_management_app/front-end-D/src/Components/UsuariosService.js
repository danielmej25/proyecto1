import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class UsuariosService{
    constructor(){}


    getUsuarios(){
        const url = `${API_URL}/api/usuarios/`;
        return axios.get(url).then(response => response.data);
    }
    getUsuariosByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    deleteUsuario(usuario){
        const url = `${API_URL}/api/usuarios/${usuario.pk}`;
        return axios.delete(url);
    }
    getUsuario(pk) {
        const url = `${API_URL}/api/usuarios/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    createUsuario(usuario){
        const url = `${API_URL}/api/usuarios/`;
        return axios.post(url,usuario);
    }
    updateUsuario(usuario){
        const url = `${API_URL}/api/usuarios/${usuario.pk}`;
        return axios.put(url,usuario);
    }

}