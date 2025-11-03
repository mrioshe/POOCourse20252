/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejerciciop418;

/**
 *
 * @author Mauricio
 */
public class EquipoMaratonProgramacion {
    
    String nombreEquipo;
    String universidad;
    String lenguajeProgramacion;
    
    Programador[] programadores;
    int tamanhoEquipo;
    
    EquipoMaratonProgramacion(String nombreEquipo, String universidad, String lenguajeProgramacion){
        this.nombreEquipo=nombreEquipo;
        this.universidad =this.universidad;
        this.lenguajeProgramacion =this.lenguajeProgramacion;
        this.programadores =this.programadores;
        tamanhoEquipo=0;
        programadores = new Programador[3];
    }
    
    boolean estaLleno(){
        return tamanhoEquipo==programadores.length;
    }
    
    void anhadir(Programador programador) throws Exception{
    
        if(estaLleno()==true){
        
            throw new Exception ("El equipo està completo. No se puedo agregar programa");
        }
        
        programadores[tamanhoEquipo]=programador;
        tamanhoEquipo=tamanhoEquipo+1;
    
        
    }
    
    static void validarCampo(String campo) throws Exception{
        for (int j=0;j<campo.length();j++){
            char c=campo.charAt(j);
            if(Character.isDigit(c)){
                throw new Exception("El nombre no puede tener digitos");
            }
        }
        if (campo.length()>20){
            throw new Exception("La longitud no debe ser superior a 20 caracteres");
        }
    }
    
}
