/*
 * This file was generated by the Gradle 'init' task.
 *
 * This generated file contains a sample Java application project to get you started.
 * For more details on building Java & JVM projects, please refer to https://docs.gradle.org/8.10/userguide/building_java_projects.html in the Gradle documentation.
 */

plugins {
    application
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(libs.junit.jupiter)
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")

    implementation(project(":external:sprite-extractor"))
    implementation(libs.guava)
}

// Apply a specific Java toolchain to ease working on different environments.
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

application {
    mainClass = "org.example.Sprite2dTK"
}

version = "1.0.0"

tasks.jar {
    archiveBaseName = "sprite_extractor_2dtk"
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
    from(configurations["runtimeClasspath"].filter { it.name.endsWith("jar") }.map { zipTree(it) })
    dependsOn(":external:sprite-extractor:jar")
    manifest {
        attributes["Main-Class"] = "org.example.Sprite2dTK"
    }
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}
