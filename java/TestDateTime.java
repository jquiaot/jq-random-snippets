import java.time.*;
import java.time.format.*;
import java.time.temporal.*;
import java.util.*;

/**
 * Test class for exercising Java 8+ Date/Time APIs.
 */
public class TestDateTime {

    //
    // helper method to trim print statements for below tests
    //

    static void p(Object x) {
        System.out.println(x);
    }

    static void p(String x) {
        System.out.println(x);
    }

    /**
     * Snippets exercising the {@link LocalDate} class. {@link LocalDate} represents a date in ISO format without time.
     */
    static void testLocalDate() {
        // create new LocalDate object that represents the date right now
        LocalDate now = LocalDate.now();
        p(now);

        // create new LocalDate object from a string
        LocalDate idesOfMarch = LocalDate.parse("2020-03-15");
        p(idesOfMarch);

        // create new LocalDate object from components of the date
        LocalDate valentinesDay = LocalDate.of(2020, 2, 14);
        p(valentinesDay);

        // compare two dates
        p("Today after Valentine's Day? " + now.isAfter(valentinesDay));
        p("Today before Valentine's Day? " + now.isBefore(valentinesDay));
        p("Ides of March after Valentine's Day? " + idesOfMarch.isAfter(valentinesDay));
        p("Ides of March equals '2020-03-15'? " + idesOfMarch.equals(LocalDate.of(2020, 3, 15)));

        // day of week
        p("Ides of March 2020 fell on a " + 
            idesOfMarch.getDayOfWeek().getDisplayName(TextStyle.FULL, Locale.getDefault()));

        // date math
        p("The day after Valentine's Day: " + valentinesDay.plusDays(1L));
        p("The week before the Ides of March: " + idesOfMarch.minusWeeks(1L));
        p("Next month: " + now.plus(Period.ofMonths(1)));
    }

    /**
     * Snippets exercising the {@link LocalTime} class. {@link LocalTime} represents time without a date.
     */
    static void testLocalTime() {
        // create new LocalTime object that represents the time right now
        LocalTime now = LocalTime.now();
        p(now);

        // create a new LocalTime object from a string
        LocalTime quarterPastNine = LocalTime.parse("09:15"); // need the leading zero
        p(quarterPastNine);

        // create a new LocalTime object from components
        LocalTime fortyTwoMinutesPastMidnight = LocalTime.of(0, 42);
        p(fortyTwoMinutesPastMidnight);

        // afternoon - use military time
        LocalTime afternoonTeaTime = LocalTime.of(16, 0);
        p(afternoonTeaTime);

        // compare two times
        p("Now after noon? " + now.isAfter(LocalTime.of(12, 0)));
        p("Now before noon? " + now.isBefore(LocalTime.of(12, 0)));

        // min, max, noon, midnight - useful constants
        p("Min time: " + LocalTime.MIN);
        p("Max time: " + LocalTime.MAX);
        p("Noon:     " + LocalTime.NOON);
        p("Midnight: " + LocalTime.MIDNIGHT);

        // time math
        p("Fifteen minutes from now: " + now.plusMinutes(15));
        p("Also 15 minutes from now: " + now.plus(15L, ChronoUnit.MINUTES));
        p("Also 15 minutes from now: " + now.plus(Duration.ofMinutes(15L)));
    }

    /**
     * Snippets exercising the {@link LocalDateTime} class. {@link LocalDateTime} represents, you guessed it, the combination of date and time.
     */
    static void testLocalDateTime() {
        // create a new LocalDateTime object that represents right now
        LocalDateTime now = LocalDateTime.now();
        p(now);

        // create a new LocalDateTime object from a string
        LocalDateTime specific1 = LocalDateTime.parse("2020-04-12T12:34:56.789");
        p(specific1);

        // create a new LocalDateTime object from components
        LocalDateTime specific2 = LocalDateTime.of(2020, Month.APRIL, 12, 12, 34, 56, 789000000);
        p(specific2);
        p(specific1.isEqual(specific2));

        // create a new LocalDateTime object from a LocalDate and LocalTime
        LocalDateTime vernalEquinox = LocalDate.parse("2020-03-19").atTime(LocalTime.parse("20:49"));
        p("Vernal equinox is " + vernalEquinox);

        // compare two datetimes
        p("Now before vernal equinox? " + now.isBefore(vernalEquinox));
        p("Now after vernal equinox?  " + now.isAfter(vernalEquinox));

        // datetime math
        p("Twenty-four hours from now: " + now.plusHours(24));
        p("Also 24 hours from now:     " + now.plus(24L, ChronoUnit.HOURS));
        p("Also 24 hours from now:     " + now.plus(Duration.ofHours(24L)));
        p("Also 24 hours from now:     " + now.plus(Period.ofDays(1)));
    }

    //
    // run all the tests
    //

    public static void main(String[] args) {
        testLocalDate();
        testLocalTime();
        testLocalDateTime();
    }
}
