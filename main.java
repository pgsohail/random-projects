
package jep;

import jep.python.MemoryManager;

#
public abstract class JepAccess {

    protected final Jep jep;

    protected JepAccess(Jep jep) {
        this.jep = jep;
    }

    protected long getThreadState() {
        return jep.getThreadState();
    }

    protected ClassLoader getClassLoader() {
        return jep.getClassLoader();
    }

    protected MemoryManager getMemoryManager() {
        return jep.getMemoryManager();
    }
}
