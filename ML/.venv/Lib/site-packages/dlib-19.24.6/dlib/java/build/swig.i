
    // Put the global functions in our api into a java class called global.
    %module global 

    %{
    #include <exception>
    #include <stdexcept>
    static JavaVM *cached_jvm = 0;

    JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM *jvm, void *reserved) {
        cached_jvm = jvm;
        return JNI_VERSION_1_6;
    }

    static JNIEnv * JNI_GetEnv() {
        JNIEnv *env;
        jint rc = cached_jvm->GetEnv((void **)&env, JNI_VERSION_1_6);
        if (rc == JNI_EDETACHED)
            throw std::runtime_error("current thread not attached");
        if (rc == JNI_EVERSION)
            throw std::runtime_error("jni version not supported");
        return env;
    }

    #include "swig_api.h"
    %}

    // Convert all C++ exceptions into java.lang.Exception
    %exception {
        try {
            $action
        } catch(std::exception& e) {
            jclass clazz = jenv->FindClass("java/lang/Exception");
            jenv->ThrowNew(clazz, e.what());
            return $null;
        }
    }

    %pragma(java) jniclasscode=%{
    static { System.loadLibrary("myproject"); }
    %}

    %include "swig_api.h"
    