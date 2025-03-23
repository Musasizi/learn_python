class Creature {
    private String name;
    private String species;
    private int powerLevel;
    private int speed;
    private String habitat;
    private String specialAbility;
    private String weakness;

    public Creature(String name, String species, int powerLevel, int speed, String habitat, String specialAbility,
            String weakness) {
        this.name = name;
        this.species = species;
        this.powerLevel = powerLevel;
        this.speed = speed;
        this.habitat = habitat;
        this.specialAbility = specialAbility;
        this.weakness = weakness;
    }

    public void describe() {
        System.out.println("Creature: " + name);
        System.out.println("Species: " + species);
        System.out.println("Power Level: " + powerLevel);
        System.out.println("Speed: " + speed);
        System.out.println("Habitat: " + habitat);
        System.out.println("Special Ability: " + specialAbility);
        System.out.println("Weakness: " + weakness);
        System.out.println("------------------------------");
    }

    public void useAbility() {
        System.out.println(name + " uses " + specialAbility + "!");
    }
}

class Dragon extends Creature {
    public Dragon(String name, int powerLevel, int speed, String habitat, String specialAbility, String weakness) {
        super(name, "Dragon", powerLevel, speed, habitat, specialAbility, weakness);
    }

    public void fly() {
        System.out.println(getName() + " spreads its wings and takes off into the sky!");
    }
}

class Elf extends Creature {
    public Elf(String name, int powerLevel, int speed, String habitat, String specialAbility, String weakness) {
        super(name, "Elf", powerLevel, speed, habitat, specialAbility, weakness);
    }

    public void stealth() {
        System.out.println(getName() + " blends into the shadows, becoming nearly invisible.");
    }
}

class Mermaid extends Creature {
    public Mermaid(String name, int powerLevel, int speed, String habitat, String specialAbility, String weakness) {
        super(name, "Mermaid", powerLevel, speed, habitat, specialAbility, weakness);
    }

    public void swim() {
        System.out.println(getName() + " glides effortlessly through the waves.");
    }
}

class Golem extends Creature {
    public Golem(String name, int powerLevel, int speed) {
        super(name, "Golem", powerLevel, speed, "Forests", "Earthquake Smash", "Dark Magic");
    }

    public void smash() {
        System.out.println(getName() + " slams the ground, causing a small earthquake!");
    }
}

public class ken {
    public static void main(String[] args) {
        Dragon drake = new Dragon("Drake", 90, 60, "Mountains", "Fire Breath", "Ice");
        Elf legolas = new Elf("Legolas", 80, 100, "Forests", "Archery Mastery", "Dark Magic");
        Mermaid ariel = new Mermaid("Ariel", 70, 80, "Oceans", "Siren Song", "Pollution");
        Golem rocky = new Golem("Rocky", 95, 30);

        drake.describe();
        drake.useAbility();
        drake.fly();

        legolas.describe();
        legolas.useAbility();
        legolas.stealth();

        ariel.describe();
        ariel.useAbility();
        ariel.swim();

        rocky.describe();
        rocky.useAbility();
        rocky.smash();
    }
}