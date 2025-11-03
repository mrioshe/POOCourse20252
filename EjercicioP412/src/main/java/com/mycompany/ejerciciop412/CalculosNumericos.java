/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejerciciop412;
import java.util.*;

/**
 *
 * @author Mauricio
 */
public class CalculosNumericos {
    
    static void calcularLogaritmoNeperiano(double valor) {
        try {
            if (valor < 0) {
                throw new ArithmeticException("El valor debe ser un número positivo");
            }

            double resultado = Math.log(valor);
            System.out.println("Resultado = " + resultado);

        } catch (ArithmeticException e) {
            System.out.println("El valor debe ser un número positivo para calcular el logaritmo");
        
            
        } catch (InputMismatchException e) {
            System.out.println("El valor debe ser numérico para calcular el logaritmo");
        }
    }
    
    
    static void calcularRaizCuadrada(double valor) {
        try {
            if (valor < 0) {
                throw new ArithmeticException("El valor debe ser un número positivo");
            }

            double resultado = Math.sqrt(valor);

            System.out.println("Resultado = " + resultado);

        } catch (ArithmeticException e) {
            System.out.println("El valor debe ser un número positivo para calcular la raíz cuadrada");

        } catch (InputMismatchException e) {
            System.out.println("El valor debe ser numérico para calcular la raíz cuadrada");
        }
    }
    
}
