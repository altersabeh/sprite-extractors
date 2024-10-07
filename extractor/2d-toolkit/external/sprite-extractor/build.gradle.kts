plugins {
    `java-library`
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(libs.commons.collections4)
    implementation(libs.commons.io)
    implementation(libs.commons.lang)
    implementation(libs.dd.plist)
    implementation(libs.everit.json.schema)
    implementation(libs.gson)
    implementation(libs.imgscalr.lib)
    implementation(libs.jackson.dataformat.xml)
    
    testImplementation(libs.junit.jupiter)
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

version = "1.1"

tasks.jar {
    archiveBaseName = "kjarrio_sprite_extractor"
}

tasks.withType<Test> {
    useJUnitPlatform()
    ignoreFailures = true
    outputs.upToDateWhen { false }
    testLogging {
        events("passed", "skipped", "failed")
        showExceptions = true
        showCauses = true
        showStackTraces = true
    }
    afterSuite(
        KotlinClosure2({ desc: TestDescriptor, result: TestResult ->
            if (desc.parent == null) {
                println("")
                val resultColor = if (result.resultType == TestResult.ResultType.SUCCESS) "\u001B[32m" else "\u001B[31m"
                print("Results: $resultColor${result.resultType}\u001B[0m, ")
                print("( Tests: ${result.testCount}, ")
                print("Passed: ${result.successfulTestCount}, ")
                print("Failed: ${result.failedTestCount}, ")
                println("Skipped: ${result.skippedTestCount} )")
            }
        }),
    )
    addTestListener(
        object : TestListener {
            override fun beforeSuite(suite: TestDescriptor) {}
            override fun afterSuite(
                suite: TestDescriptor,
                result: TestResult,
            ) {}
            override fun beforeTest(testDescriptor: TestDescriptor) {}
            override fun afterTest(
                testDescriptor: TestDescriptor,
                result: TestResult,
            ) {
                if (result.resultType == TestResult.ResultType.FAILURE) {
                    val exceptions = result.exceptions
                    if (exceptions.isNotEmpty()) {
                        println("\nTest: ${testDescriptor.name} - ${result.resultType}")
                        exceptions.forEach { exception ->
                            println(exception.message)
                        }
                    }
                }
            }
        },
    )
}
