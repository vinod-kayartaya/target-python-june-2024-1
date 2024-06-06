package com.targetindia.programs;

import com.targetindia.model.Circle;
import com.targetindia.model.Shape;

public class TestingPolymorphism {

    static void processShape(Shape shape){

    }

    public static void main(String[] args) {

        Circle c1 = new Circle();
        processShape(c1);

        String s1 = "Vinod";
        processShape(s1);

    }
}
