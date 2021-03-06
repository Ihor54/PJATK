package participants;

import common.TestUtils;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.lang.reflect.Method;
import java.net.*;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class WebPageMonitorTest extends TestUtils {

    @Test
    public void updateLastModifiedTest() throws Exception {
        Method updateLastModified = WebPageMonitor.class.getDeclaredMethod("updateLastModified", URL.class);
        updateLastModified.setAccessible(true);
        /*
         * before updating the dates for the first time all of them should be null
         * */
        observers.forEach(o -> Assert.assertEquals((long) responses[0], o.getLastModified().getTime()));
        for (URL url : urls) {
            updateLastModified.invoke(monitor, url);
        }
        /*
         * updating change dates and check if they were set correctly
         * */
        for (int i = 3; i < responses.length; i++) { // starting with 3 because mockito starts returning responses from 3 index
            for (URL url : urls) {
                updateLastModified.invoke(monitor, url);
            }
            for (IObserver o : observers) {
                Assert.assertEquals((long) responses[i], o.getLastModified().getTime());
            }
        }
    }

}